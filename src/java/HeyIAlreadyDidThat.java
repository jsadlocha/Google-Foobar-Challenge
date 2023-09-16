import java.util.Arrays;
import java.util.HashMap;

public class HeyIAlreadyDidThat {
  public static void main(String[] args) {
    assert solution("1211", 10) == 1;
    assert solution("210022", 3) == 3;
    System.out.print("All tests passes!");
  }

  public static int solution(String n, int b) {
    var k = n.length();
    var n__ = n.toCharArray();
    Arrays.sort(n__);
    var x = Integer.parseInt(new String(n__), b);
    var y = Integer.parseInt(new StringBuilder(new String(n__)).reverse().toString(), b);
    var z = y - x;
    var n_ = Integer.toUnsignedString(z, b);
    if (Integer.parseInt(n_, b) == 0)
      return 1;

    var minionHashMap = new HashMap<String, Integer>();
    minionHashMap.put(n, 1);
    if (minionHashMap.containsKey(n_))
      return 1;

    minionHashMap.put(n_, 2);
    var i = 3;
    while (true)
    {
      n__ = n_.toCharArray();
      Arrays.sort(n__);
      x = Integer.parseInt(new String(n__), b);
      y = Integer.parseInt(new StringBuilder(new String(n__)).reverse().toString(), b);
      if (n__.length != k)
        y *= b;
      z = y - x;
      if (z == 0)
        return 1;

      n_ = Integer.toUnsignedString(z, b);
      if (minionHashMap.containsKey(n_))
        return i - minionHashMap.get(n_);

      minionHashMap.put(n_, i);
      i+=1;
      if (i == 10000) // bypass for unreachable statment
        break;
    }
    return 0;
  }
}
