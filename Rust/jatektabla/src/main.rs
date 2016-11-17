use	std::io::{self, BufRead};

fn main() {
	//Read
    let stdin = io::stdin();
    let input = stdin.lock().lines().nth(1).unwrap().unwrap();
    let input = input.split(' ').map(|x| x.parse::<i32>().unwrap()).collect::<Vec<_>>();

    //Compute
    let mut out = Vec::new();
    for x in input {
        match x {
            0 | 1 | 2 => out.push(x),
            3 => {out.pop();},
            4 => for y in out.iter_mut().rev() {
                match *y {
                    0 => *y = 2,
                    1 => {*y = 0; break;},
                    2 => {*y = 1; break;},
                    _ => panic!(),
                };
            },
            5 => for y in out.iter_mut().rev() {
                match *y {
                    0 => {*y = 1; break;},
                    1 => {*y = 2; break;},
                    2 => *y = 0,
                    _ => panic!(),
                };
            },
            _ => panic!(),
        };
	}

	//Write
	println!("{}", out.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
}