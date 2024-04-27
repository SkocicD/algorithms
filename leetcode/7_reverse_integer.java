import java.util.Stack;

class Solution {
    public int reverse(int x) {
        boolean negative = (x < 0);
        x = Math.abs(x);
        long y = 0, i = 1;
        Stack<Integer> s = new Stack<Integer>();
        int numdigits = 0;
        while (x > 0)
        {
            s.push (x % 10);
            x /= 10;
            numdigits++;
        }
        for (int j = 0; j < numdigits; j++)
        {
            y += i * s.pop();
            i *= 10;
        }
        if (y > ((1 << 31) - 1)) return 0;
        if (negative) y *= -1;
        return (int)y;
    }
}

