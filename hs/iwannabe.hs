import Data.List

main = interact (writeOutput . solve . readInput)

readInput :: String -> (Int, [(Int, Int, Int)])
readInput s = (k, map toTriplet ls)
    where
        (n:k:[]) = map read (words (head (lines s)))
        ls = tail (lines s)
       

toTriplet :: String -> (Int, Int, Int)
toTriplet s = listToTriplet (map read (words s))
    where 
        listToTriplet :: [Int] -> (Int, Int, Int)
        listToTriplet (x:y:z:[]) = (x, y, z)


writeOutput :: Int -> String
writeOutput = (++"\n") . show


solve :: (Int, [(Int, Int, Int)]) -> Int
solve (k, p) = length $ group $ sort $ (buildTeamWithDuplicates k p)

buildTeamWithDuplicates :: Int -> [(Int, Int, Int)] -> [(Int, Int, Int)]
buildTeamWithDuplicates k p = (take k (sortBy orderFirst p)) ++ (take k (sortBy orderSecond p)) ++ (take k (sortBy orderThird p))

orderFirst :: (Int, Int, Int) -> (Int, Int, Int) -> Ordering
orderFirst (a, b, c) (d, e, f)
    | a > d = LT
    | otherwise = GT

orderSecond :: (Int, Int, Int) -> (Int, Int, Int) -> Ordering
orderSecond (a, b, c) (d, e, f)
    | b > e = LT
    | otherwise = GT

orderThird :: (Int, Int, Int) -> (Int, Int, Int) -> Ordering
orderThird (a, b, c) (d, e, f)
    | c > f = LT
    | otherwise = GT
