#include <gtest/gtest.h>
#include <string>
#include <vector>
#include <algorithm>

// Example function to test
int add(int a, int b) {
    return a + b;
}

bool isPalindrome(const std::string& s) {
    std::string rev = s;
    std::reverse(rev.begin(), rev.end());
    return s == rev;
}

int maxElement(const std::vector<int>& arr) {
    if (arr.empty()) return -1;
    return *std::max_element(arr.begin(), arr.end());
}

// Unit tests
TEST(MathTests, AddTest) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(-1, 1), 0);
    EXPECT_EQ(add(-5, -7), -12);
}

TEST(StringTests, PalindromeTest) {
    EXPECT_TRUE(isPalindrome("madam"));
    EXPECT_TRUE(isPalindrome("racecar"));
    EXPECT_FALSE(isPalindrome("hello"));
}

TEST(VectorTests, MaxElementTest) {
    EXPECT_EQ(maxElement({1, 2, 3, 4, 5}), 5);
    EXPECT_EQ(maxElement({-5, -2, -9}), -2);
    EXPECT_EQ(maxElement({}), -1);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
