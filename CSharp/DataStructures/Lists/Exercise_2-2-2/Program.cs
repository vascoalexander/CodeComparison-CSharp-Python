List<int> lst = new List<int> { };
for (int i = 0; i < 11; i += 2)
{
    lst.Add(i);
}
foreach (int i in lst)
{
    Console.Write(i + " ");
}
