package com.zer0rez.euler.problems

import com.zer0rez.euler.Problem
import com.zer0rez.euler.Solution

class Problem9 : Problem {
    override fun solve(): Solution {
        var triplet: Triple<Int, Int, Int>? = null
        for (s1 in 1..1000) {
            for (s2 in s1..1000 - s1) {
                for (s3 in s2..1000 - s1 - s2) {
                    if (s1 + s2 + s3 == 1000 && s1 * s1 + s2 * s2 == s3 * s3) {
                        triplet = Triple(s1, s2, s3)
                        break;
                    }
                }
                if (triplet != null) break
            }
            if (triplet != null) break;
        }
        val answer = triplet!!.first * triplet.second * triplet.third
        // a+b+c = 100, a^2 + b^2 = c^2
        return Solution(9, answer.toString(), "${triplet}")
    }
}