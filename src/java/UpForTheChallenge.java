import java.util.Arrays;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class UpForTheChallenge {
    public static void main(String[] args) {
        String inp = "01100110 01101001 01101110 01100100 00101110 01100110 01101111 01101111 00101111 01100101 01101101 01100101 01100001 01100011 01101000 01100001 01101100 01101100 01100101 01101110 01100111 01100101 00110010 00110011";
        Stream<String> stream = Arrays.stream(inp.split(" "));
        String out = stream.map(num -> (char)Integer.parseInt(num, 2))
                .map(Objects::toString)
                .collect(Collectors.joining(""));
        System.out.println(out);
    }
}
