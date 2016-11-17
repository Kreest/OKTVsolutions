use std::io::{self, BufRead};

fn main() {
    let mut number = String::new();
    io::stdin().read_line(&mut number).unwrap();
    let number = number.trim().parse::<i64>().unwrap();
    println!("{}", iterative(number));
}
fn iterative(x: i64) -> i64 {
	let mut a: i64 = 1;
	let mut b: i64 = 1;
	let mut c: i64 = 0;
	for i in 3..(x+1) {
		c = (i-1)*b + (i-2)*a;
		a = b;
		b = c;
	}
	c
}
