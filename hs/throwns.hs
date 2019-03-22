main = interact (writeOutput . solve . readInput)

readInput :: String -> (Int, [String])
readInput s = extract (words s)

extract :: [String] -> (Int, [String])
extract (n:k:tokens) = (read n, tokens)

writeOutput :: Int -> String
writeOutput = (++"\n") . show

solve :: (Int, [String]) -> Int
solve (n, tokens) = head (solveAux n tokens [0])

solveAux :: Int -> [String] -> [Int] -> [Int]
solveAux n [] stack = stack
solveAux n (t:[]) stack = (throw n (read t) (head stack)):stack
solveAux n (t:tt:ts) stack
    | t == "undo" = solveAux n ts (drop (read tt) stack)
    | otherwise = solveAux n (tt:ts) ((throw n (read t) (head stack)):stack)

throw :: Int -> Int -> Int -> Int
throw n d curr = (curr + d) `mod` n