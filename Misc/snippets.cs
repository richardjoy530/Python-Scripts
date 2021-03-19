static void Main(string[] args)
{
    Console.WriteLine("Hello World");

    download();
    
    Console.ReadLine();
}

static void download()
{
    Task.Run(() => {

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Tick");
            Thread.Sleep(1000);
        }

    });
}

-------------------------

static void Main(string[] args)
{
    Console.WriteLine("Hello World");

    download();
    
    Console.ReadLine();
}

static async void download()
{
    await Task.Run(() => {

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Tick");
            Thread.Sleep(1000);
        }

    });

    Console.WriteLine("Completed Ticking");
}


------------------------


static async void downloadSimulator()
{
    await Task.Run(() => {

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Tick");
            Thread.Sleep(1000);
        }

    });

    Console.WriteLine(" First Completed Ticking");

    _ = Task.Run(() =>
    {

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Tick * ");
            Thread.Sleep(1000);
        }

    });

    _ = Task.Run(() =>
    {

        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine("Tick # ");
            Thread.Sleep(1000);
        }

    });
}