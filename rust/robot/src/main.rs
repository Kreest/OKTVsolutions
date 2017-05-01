use std::io::{self, BufRead};
use std::collections::HashMap;
use std::cmp;
fn main() {
	//Read
	let stdin = io::stdin();
	let mut lines = stdin.lock().lines();

    let header = lines.next().unwrap().unwrap();
    let moves = header.split(" ").nth(1).unwrap().parse::<usize>().unwrap();

    let mut apples : HashMap<[usize; 2], usize>= HashMap::new();
    for (i, l) in lines.enumerate() {
    	let l = l.unwrap().split(" ").map(|x| x.parse::<usize>().unwrap()).collect::<Vec<_>>();
    	let l = [l[0], l[1]];
        if l[0] + l[1] <= moves + 2 {apples.insert(l, i+1);}
    }
    //Calc each square's max
    let mut grid : Vec<Vec<usize>>= vec![vec![0; moves+2]; moves+2];
    for x in 1..(moves+2) {
    	for j in 1..(moves+3-x) {
    	    grid[x][j] = cmp::max(grid[x-1][j], grid[x][j-1]);
    	    if apples.contains_key(&[x, j]) {
    	    	grid[x][j] += 1;
    	    }
    	}
    }
    if cfg!(debug) {
		println!("{:?}", grid);   
    }

    //Get max at diagonal
    let mut max = 0;
    let mut maxcoords = [0, 0];
    for i in 1..moves+2 {
    	if grid[i][moves+2-i] > max {
    		max = grid[i][moves+2-i];
    		maxcoords = [i, moves+2-i];
		}
    }

    if cfg!(debug) {
		println!("{:?}, {:?}", max, maxcoords);   
    }

    //Backtrack
    let mut path = Vec::new();
    let mut coords = maxcoords;
    while coords != [1, 1] {
    	if cfg!(debug) {
    		println!("{:?}", coords);	
    	}
    	if let Some(x) = apples.get(&coords) {
    	    path.push(x)
    	}
    	if (coords[0] - 1 != 0) && grid[coords[0]][coords[1]] == grid[coords[0]-1][coords[1]] {
    	    coords = [coords[0]-1, coords[1]];
    	}
    	else if (coords[1] - 1 != 0) && grid[coords[0]][coords[1]] == grid[coords[0]][coords[1]-1] {
    	    coords = [coords[0], coords[1]-1];
    	}
    	else if (coords[0] - 1 != 0) && (grid[coords[0]][coords[1]] - 1 == grid[coords[0]-1][coords[1]]) {
    	    coords = [coords[0]-1, coords[1]];
    	}
    	else if coords[1] - 1 != 0 && grid[coords[0]][coords[1]] - 1 == grid[coords[0]][coords[1]-1] {
    	    coords = [coords[0], coords[1]-1];
    	}
    }
    if cfg!(debug) {
    	println!("{:?}", path);
    }

    //Print
    println!("{}", path.len());
    println!("{}", path.iter().map(|x| x.to_string()).rev().collect::<Vec<_>>().join(" "));
}