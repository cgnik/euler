package com.zer0rez.euler.util

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class UtilTest {

    @Test
    fun isDivisibleByAll() {
        assertTrue(8.isDivisibleByAll(intArrayOf(2, 1)))
        assertTrue(9.isDivisibleByAll(intArrayOf(3, 1)))
        assertTrue(99.isDivisibleByAll(intArrayOf(33, 9, 11, 1)))
    }

    @Test
    fun isDivisibleBy() {
        assertFalse(1.isDivisibleBy(2))
        assertFalse(3.isDivisibleBy(2))
        assertTrue(1.isDivisibleBy(1))
    }

    @Test
    fun swapinShiftsAndAdds() {
        var example = intArrayOf(32, 73)
        val result = example.swapin(832)
        assertArrayEquals(intArrayOf(73, 832), example)
        assertEquals(result, 832)
    }

    @Test
    fun fibonacci() {
        assertArrayEquals(intArrayOf(1, 1, 2, 3, 5), fibonacci { v -> v > 5 })
    }

    @Test
    fun factorize() {
//        var result = 10L.factorize().toList().toLongArray()
//        assertArrayEquals(longArrayOf(5, 2), result)
//        result = 13L.factorize().toList().toLongArray()
//        assertArrayEquals(longArrayOf(), result)
//        result = 22L.factorize().toList().toLongArray()
//        assertArrayEquals(longArrayOf(2, 11), result)
//        result = 40L.factorize().toList().toLongArray()
//        assertArrayEquals(longArrayOf(2, 5), result)
    }

    @Test
    fun isPalindrome() {
        // for the purposes of these tests, single-digits are non-palindromic
        assertFalse(0.isPalindrome())
        assertFalse(7.isPalindrome())
        assertTrue(101.isPalindrome())
        assertTrue(12344321.isPalindrome())
        assertTrue(1234321.isPalindrome())
        assertTrue(990099.isPalindrome())
        assertFalse(998099.isPalindrome())
    }
}