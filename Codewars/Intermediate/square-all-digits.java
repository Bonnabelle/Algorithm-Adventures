public class SquareDigit {

  String fin = "";
  int cur;

  public int squareDigits(int n) {
    while(n > 0) {
        cur = n%10;
        fin += Integer.toString(cur * cur);
        n = n / 10;
     } return Integer.parseInt(fin);
  }

}

/*
Apparently this kata has had issues for a year with random tests. Passed all normal ones, sensei won't fix the random tests.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*/
