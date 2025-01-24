public class TreeNode{

	TreeNode left = null;
	TreeNode right = null;
	int length;
	String value;

	public TreeNode(String value){
		this.value = value;
		this.length = 0;
	}

	public TreeNode getLeft(){
		return left;
	}
	public TreeNode getRight(){
		return right;
	}
	public void setLeft(TreeNode left){
		this.left = left;
	}
	public void setRight(TreeNode right){
		this.right = right;
	}

}

