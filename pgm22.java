import java.util.*;
public class pgm22 {
    public static void main(String[] args) {

        char s1[] = {'a','b','c','d'};
        char s2[] = {'d','b','c','a'};

        Arrays.sort(s1);
        Arrays.sort(s2);

        int n1 = s1.length;
        int n2 = s2.length;

        boolean a = false;

        for(int i=0; i<n1; i++){
            if(s1[i] == s2[i]){
               a = true;
            }
            if(s1[i] != s2[i]){
                a = false;
                break;
            }
        }

        if(a){
            System.out.println("Strings are anagram of each other");
        }
        else{
            System.out.println("Strings are not anagrams of each other");
        }



    }
}
