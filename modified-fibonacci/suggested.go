func fibonacciModified(t1 *big.Int, t2 *big.Int, n int) *big.Int {

    for i := 2; i <= n; i++ {
        temp := new(big.Int).Set(t2)
        t2.Add(t1, new(big.Int).Mul(t2, t2))
        t1.Set(temp)
    }
    return t1
}