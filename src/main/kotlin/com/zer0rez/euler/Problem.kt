package com.zer0rez.euler

interface Problem {
    fun solve(): Solution
}

data class Solution (
    val number: Long,
    val answer: String,
    val extra: String
)