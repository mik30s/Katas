package main
import  (
	"fmt",
 	"sort"
)

// rudimentary insertion sort
func insertion_sort(list []int) []int {
	for i := 1; i < len(list); i++ {
		fmt.Printf("%v", i)
		j := i - 1
		for j > 0 {
			if list[j] > list[j + 1] {
				temp := list[j + 1]
				list[j + 1] = list[j]
				list[j] = temp
				j--
			}
		}
	}
	return list
}

func binary_search(list []int) {
	// first sort it.

}

func main() {
	fmt.Printf("%v", insertion_sort([]int{1,3,4,2}))
}