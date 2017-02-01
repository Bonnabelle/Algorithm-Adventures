public class Solution {
    //Provided code
   public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases>0){
         String username = in.nextLine();

         //User code
         String pattern = "^[a-zA-Z]\\w{7,29}$";

         Pattern r = Pattern.compile(pattern);
         Matcher m = r.matcher(username);

    //More provided
         if (m.find( )) {
            System.out.println("Valid");
         } else {
            System.out.println("Invalid");
         }
         testCases--;
      }
   }
}

/*

Regular expressions (regexp) help us match or search for patterns in strings. In this problem, you will be given a username. Your task is to check whether that username is valid. A valid username will have the following properties:

The username can contain alphanumeric characters and/or underscores(_).
The username must start with an alphabetic character.
8 <= |Username| <= 30.
To simplify your task, we have provided a portion of the code in the editor. You just need to write down pattern compilation.

*/
