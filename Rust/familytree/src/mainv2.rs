use std::io::{self, BufRead};
use std::collections::{HashSet, HashMap};

fn main() {
	//Read
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let header = input.next();
    let header = header.unwrap().unwrap();
    let header = header.split(" ").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>(); 	//Get header info

    let mut nodes : HashMap<i32, Vec<i32>> = HashMap::new();								//Collect every node with parents into a hashmap
    for _ in 0..header[1] {
        let push = input.next();
        let push = push.unwrap().unwrap();
        let push = push.split(" ").map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>();
        nodes.insert(push[0], vec![push[1], push[2]]);
    }

    //Compute
    	//Get childless nodes
    let baseset : HashSet<_> = (1..21).collect();
    let set1 : HashSet<_> = nodes.values().map(|x| x[0]).collect();
    let set2 : HashSet<_> = nodes.values().map(|x| &x[1]).collect();

    let childless = baseset.difference(&set1).collect::<HashSet<_>>();
    let childless = childless.difference(&set2).map(|x| **x).collect::<HashSet<_>>();

   		//Collect the ancestors of each childless node 
   	let mut ancestries : Vec<Vec<i32>> = Vec::new();
    for node in childless {
    	let mut ancestors : Vec<i32> = Vec::new();
    	let mut stack : Vec<i32> = Vec::new();
    	stack.push(node);

    	while !stack.is_empty() {
    		let v : i32 = stack.pop().unwrap();
    		if nodes.contains_key(&v) {
    		    for x in nodes.get(&v).unwrap() {
    		        stack.push(*x);
    		        ancestors.push(*x);
    		    }
    		}
		}
		
		ancestries.push(ancestors);
	}

		//Find the union of all parent sets
	let ancestries : Vec<HashSet<_>>= ancestries.iter().map(|x| x.iter().cloned().collect()).collect();
    let baseset : HashSet<_> = (1..21).collect();
	let common = ancestries.iter().fold(baseset,|folded, x| folded.intersection(x).cloned().collect());

	//Print
	let mut common : Vec<_> = common.iter().collect();
	common.sort();
	println!("{}", common.len());
	for x in common {
	    print!("{} ", x);;
	}
}
