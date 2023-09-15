import java.util.ArrayList;
import java.util.Arrays;

public class GearingUpForDestruction {
  public static void main(String[] args) {
    assert Arrays.equals(solution(new int[] {4, 13}), new int[] {6, 1});
    assert Arrays.equals(solution(new int[] {4, 17, 50}), new int[] {-1, -1});
    assert Arrays.equals(solution(new int[] {4, 30, 50}), new int[] {12, 1});
    assert Arrays.equals(solution(new int[] {4, 30, 50, 62}), new int[] {12, 1});
    System.out.println("All tests passes!");
  }

    public static int[] solution(int[] pegs) {
    var even = pegs.length % 2 == 0;

    var distances = new ArrayList<Integer>();
    for (int i = 0; i < pegs.length - 1; i++)
    {
      var dist = pegs[i+1] - pegs[i];
      var eq = i % 2 == 0 ? dist : -1 * dist;
      distances.add(eq);
    }
    var sum = distances.stream().reduce(Integer::sum).get();
    var last_gear = even ? sum/3 : sum;
    var first_gear = 2 * last_gear;

    var gear = first_gear;
    for (var el : distances){
      gear = Math.abs(el) - gear;
      if (gear < 1)
        return new int[] {-1, -1};
    }

    sum *= 2;
    if (even)
    {
        if (sum % 3 == 0)
            return new int[] {sum/3, 1};
        return new int[]{sum, 3};
    }

    return new int[]{sum, 1};
  }
}
