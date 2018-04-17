open Printf

(* let (--) i j = 
    let rec aux n acc =
      if n < i then acc else aux (n-1) (n :: acc)
    in aux j [] ;; *)

(* let print_list a = function 
    List.iter (printf "%d ") a ;;

print_list [1;3;5] ;;
let a = [1;2;3;4;5]
let () = List.iter (printf "%d ") a *)
(* let my_list = [1;2;3]
let rec f elem = function
    printf "I'm looking at element %d now\n" elem in
    List.iter f my_list;; *)
(* let help =
    List.map (fun x -> x + 1) [3; 5; 7; 9];;

printf help *)




(* let rec reverse (l: 'a list) : 'a list =
    match l with
    [] -> []
    | hd :: tl -> (reverse tl) @ [hd];; *)

let square a = [] ;;
printf("%l") (square "yo") ;;
