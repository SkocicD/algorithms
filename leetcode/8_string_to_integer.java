import java.util.Stack;

class Solution {
    public int myAtoi(String s) {
        boolean negative = false, first = true, firstnum = false;
        long num = 0, i = 1, j = 0;
        Stack<Character> stk = new Stack<Character>();
        char[] arr = s.toCharArray();
        for (char c: arr)
        {
            if (!Character.isDigit(c))
            {
                if (firstnum) break;
                if (first)
                {
                    if (c == ' ') continue;
                    first = false;
                    if (c == '-'){
                        negative = true;
                        continue;
                    }
                    else if (c == '+')
                        continue;
                    else break;
                }
                else break;
            }
            
            //if (c == '0' && !firstnum)
            //    first = false;
            if (c != '0' || firstnum) {
                firstnum = true;
                stk.push(c);
                j++;
            }
            first = false;

        }
        for (int k = 0; k < j; k++)
        {
            num += ((int)stk.pop()-48) * i;
            i*=10;
        }
        if (j > 10 || num > (1 << 31) - 1) 
        {
            num = (1 << 31) - 1;
            if (negative)
                num++;
        }
        if (negative)
            return (int)(-1*num);
        else 
            return (int)num;
    }
}
