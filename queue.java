import java.util.Scanner;
import java.util.ArrayList;

public class queue {
    public static void main(String[] args) {
        try (Scanner scanner_in = new Scanner(System.in)) {
            /*
             * Read size input
             */
            int input_size = Integer.parseInt(scanner_in.nextLine());

            /*
             * Read customer waiting times
             */
            ArrayList<Integer> customer_waiting_times = new ArrayList<>();
            String elem_inputs[] = scanner_in.nextLine().split(" ");
            for (String elem : elem_inputs) {
                customer_waiting_times.add(Integer.parseInt(elem));
            }

            /*
             * Sort customer waiting times
             * O(nlogn)
             */
            customer_waiting_times.sort(null);

            /*
             * The customer is satisfied if
             * the elapsed time before him (sum of waiting times prior)
             * is less that his waiting limit
             */
            int elapsed = 0;
            int satisfy_customers = 0;
            // use iterator instead of while loop + index access
            
            // NOT OPTIMIZED: while loop + ArrayList access is O(n^2)
            // int i = 0;
            // while (i < input_size) {
            //     // Remove customer if cannot serve in time
            //     if (elapsed > customer_waiting_times.get(i)) {
            //         customer_waiting_times.remove(i);
            //         --input_size;
            //         continue;
            //     } else {
            //         ++satisfy_customers;
            //         elapsed += customer_waiting_times.get(i);
            //         ++i;
            //     }
            // }

            // NOT OPTIMIZED: unsatisfy customers increase unnecessary waiting time
            // for (int time : customer_waiting_times) {
            // if (elapsed <= time) {
            // ++satisfy_customers;
            // }
            // elapsed += time;
            // }

            System.out.print(satisfy_customers);
        }
    }
}