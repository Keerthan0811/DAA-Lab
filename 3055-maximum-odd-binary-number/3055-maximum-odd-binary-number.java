class Solution {
    public String maximumOddBinaryNumber(String s) {
        int count = 0;
        for(char ch : s.toCharArray())
            if(ch == '1') count++;

        int n = s.length();
        char[] arr = new char[n];

        for(int i=0; i<n; i++)
            arr[i] = '0';

        arr[n-1] = '1';
        count--;

        int i=0;
        while(count-- > 0)
            arr[i++] = '1';

        return new String(arr);
    }
}