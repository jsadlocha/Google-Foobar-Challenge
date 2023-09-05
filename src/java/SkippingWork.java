import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SkippingWork {
    public static int Solution (int[] x, int[] y) {
        Set<Integer> set1 = IntStream.of(x).boxed().collect(Collectors.toSet());
        Set<Integer> set2 = IntStream.of(y).boxed().collect(Collectors.toSet());
        Set<Integer> diff = new HashSet<Integer>(set1);
        diff.addAll(set2);
        set1.retainAll(set2);
        diff.removeAll(set1);
        return diff.stream().findFirst().get();
    }
}
