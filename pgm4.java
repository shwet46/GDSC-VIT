public class pgm4 {

    public static void remove_chars(String s, int n){
        String m = s.substring(n);
        System.out.println(m);
    }

    public static void main(String[] args) {

        remove_chars("pynative",4);
        remove_chars("pynative",2);

    }
}
