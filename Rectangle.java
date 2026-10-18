public class Rectangle{

	public static void main(String[] args){
		
		
	for(int index = 1; index <= 5; index++){
	
		for(int count=1; count <= 5; count++){
		
			if(index == 1 || index ==5){
		
				System.out.print("*");
			}
			else{
				if(count ==1 || count ==5){
					System.out.print("*");
				}
				else{
					System.out.print(" ");
				}
			
			}
			
		}
					System.out.println();
	}
   }
}
