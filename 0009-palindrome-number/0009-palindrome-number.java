import java.lang.StringBuilder;
import java.util.List;


class Solution {
    public boolean isPalindrome(int x) {



        String x2s = new String(Integer.valueOf(x).toString());

        int ln = Integer.valueOf(x).toString().length();
        
        StringBuilder sb = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();

        for(int i = 0; i < ln; i++){
            sb.append(x2s.charAt(i));
        }

        for(int i = ln - 1; i > -1; i--){
            sb2.append(x2s.charAt(i));
        }

        System.out.println(sb);
        System.out.println(sb2);

        System.out.println(sb.equals(sb2));

        if (sb.toString().equals(sb2.toString())){
            return true;
        }else{
            return false;
        }
        
    }
}