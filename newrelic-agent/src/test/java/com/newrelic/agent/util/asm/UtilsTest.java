/*
 *
 *  * Copyright 2020 New Relic Corporation. All rights reserved.
 *  * SPDX-License-Identifier: Apache-2.0
 *
 */

package com.newrelic.agent.util.asm;

import java.io.IOException;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ScheduledExecutorService;
import java.util.function.Predicate;

import javax.sql.PooledConnection;
import javax.swing.ListCellRenderer;

import com.newrelic.agent.bridge.AgentBridge;
import org.junit.Assert;
import org.junit.Test;
import org.objectweb.asm.ClassReader;
import org.objectweb.asm.Type;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class UtilsTest {

    @Test
    public void getAnnotationsMatcher() {
        Predicate<Class> annotationsMatcher = Utils.getAnnotationsMatcher(Type.getDescriptor(Test.class)::equals);
        assertTrue(annotationsMatcher.test(UtilsTest.class));
        assertFalse(annotationsMatcher.test(AgentBridge.class));
        assertFalse(annotationsMatcher.test(Runnable.class));
    }

    @Test
    public void readClassThroughLoader() throws IOException {
        ClassReader classReader = Utils.readClass(UtilsTest.class.getClassLoader(),
                Type.getInternalName(BadMethodMatch.class));
        assertClass(classReader);
    }

    @Test
    public void readClass() throws IOException {
        ClassReader classReader = Utils.readClass(BadMethodMatch.class);
        assertClass(classReader);
    }

    @Test(expected = BenignClassReadException.class)
    public void readClassArray() throws IOException {
        Utils.readClass(BadMethodMatch[].class);
    }

    @Test(expected = BenignClassReadException.class)
    public void readClassProxy() throws IOException {
        Class<?> proxyClass = Proxy.getProxyClass(getClass().getClassLoader());
        Utils.readClass(proxyClass);
    }

    @Test
    public void getClassResourceName() {
        Assert.assertEquals("java/util/List.class", Utils.getClassResourceName(List.class));
    }

    @Test
    public void getClassResourceName_FromInternal() {
        Assert.assertEquals("java/util/List.class", Utils.getClassResourceName("java/util/List"));
    }

    private void assertClass(ClassReader classReader) {
        assertTrue(Arrays.asList(classReader.getInterfaces()).contains(Type.getInternalName(Map.class)));
        assertTrue(Arrays.asList(classReader.getInterfaces()).contains(
                Type.getInternalName(ListCellRenderer.class)));
        Assert.assertEquals(Type.getInternalName(LinkedHashMap.class), classReader.getSuperName());
    }

    abstract class BadMethodMatch extends LinkedHashMap implements Map, ListCellRenderer, Runnable, InvocationHandler,
            PooledConnection, ScheduledExecutorService {

        public void test() {

        }

        public ResultSet executeQuery() throws SQLException {
            return null;
        }
    }
}
