import java.util.*;

class millionairemadness{
    static HashSet<Integer> visited = new HashSet<Integer>();
    static int rows, cols;
    static long board[];
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        rows = sc.nextInt(); cols = sc.nextInt();
        board[] = new long[rows*cols];
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                board[r*cols+c] = sc.nextInt();

        

        while (!visited.contains(0)){
            visited.add(0);
        }

        System.out.println("yay");

    }
    public static void addNeighbors(TreeMap<Long, ArrayList<Integer>> neighbors, int loc){
        int right, left, up, down;
        up = loc-cols;
        down = loc+cols;
        right = r*cols+(c+1);
        left = r*cols+(c-1);

        if (up > 0 && !visited.contains(uo))
            if (neighbors.contains(
                neighbors.set(board[
    }
}
