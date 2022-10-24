// A node js solution to the 100 doors problem#A solution to the 100 doors problem

const opened = (function doors (door, n) {
    if(n === 101)
        return door;
    for(let i = n; i < 100; i++)
        if ((i + 1) % n === 0)
            door[i] = door[i] === 1 ? 0 : 1;
    return doors(door, n + 1);
}([...new Array(100)].map(() => 1), 1))

opened.forEach((element, index) => { if(element === 1 ) process.stdout.write(index + 1 + " "); })