import java.util.TreeMap;
import java.util.Scanner;
class bing{

	public static void main(String[] args){

		Scanner scan = new Scanner(System.in);

		TreeMap<String, Integer> map = new TreeMap<>();
		char afterZ = 'z' + 1;
		int count;

		int n = scan.nextInt();
		String word;
		for (int i = 0; i < n; i++){
			count = 0;			
			word = scan.next();
			for (int entry: map.subMap(word, word + afterZ).entrySet())
				count += entry;
			System.out.println(count);

			if (!map.containsKey(word))
				map.put(word, 1);
			else
				map.put(word, map.get(word)+1);
			
		}

	}

}
