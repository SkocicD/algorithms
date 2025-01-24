import java.util.Scanner;
public class bing2{
	public static void main(String[] args){
		
		Scanner scan  = new Scanner(System.in);
		String word;
		TreeNode root = null;

		int n = scan.nextInt();
		for (int i = 0; i < n; i++){
			word = scan.next();
			if (root == null)
				root = new TreeNode(word);
			else
				add(root, word);
		}
		System.out.println(root.length);
		System.out.println(root.getRight().length);
		System.out.println(root.getRight().length);

	}

	static void add(TreeNode root, String value){
		if (root == null){
			root = new TreeNode(value);
			return;
		}
		TreeNode curr = root;
		while (curr!=null){
			curr.length++;
			if (root.value.compareTo(value) < 0)
				if (curr.getLeft() == null){
					curr.setLeft(new TreeNode(value));
					return;
				}
				else
					curr = curr.getLeft();
			else
				if (curr.getRight() == null){
					curr.setRight(new TreeNode(value));
					return;
				}
				else
					curr = curr.getRight();
		}
	}

}
