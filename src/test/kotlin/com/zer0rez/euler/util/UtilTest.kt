package com.zer0rez.euler.util

import com.zer0rez.euler.util.Util.swapin
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class UtilTest {

    @Test
    fun swapinShiftsAndAdds() {
        var example = intArrayOf(32, 73)
        val result = swapin(example, 832)
        assertArrayEquals(intArrayOf(73, 832), example)
        assertEquals(result, 832)
    }

    @Test
    fun fibonacci() {
        assertArrayEquals(intArrayOf(1, 1, 2, 3, 5), Util.fibonacci { v -> v > 5 })
    }

    @Test
    fun factorize() {
        var result = Util.factorize(10L).toList().toLongArray()
        assertArrayEquals(longArrayOf(2, 5), result)
    }

    @Test
    fun isPalindrome() {
        // for the purposes of these tests, single-digits are non-palindromic
        assertFalse(Util.isPalindrome(0))
        assertFalse(Util.isPalindrome(7))
        assertTrue(Util.isPalindrome(101))
        assertTrue(Util.isPalindrome(12344321))
        assertTrue(Util.isPalindrome(1234321))
        assertTrue(Util.isPalindrome(990099))
        assertFalse(Util.isPalindrome(998099))
    }
}