using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

// runnable in .NET 5+ only
async Task Main()
{
    Console.WriteLine("Hello");
    Console.WriteLine(await GetDadJoke());
    Console.WriteLine("Bye bye");
}

async Task<string> GetDadJoke()
{
    using (var client = new HttpClient()) // I know ... I know ... It's just a demo!
    {
        client.DefaultRequestHeaders.Add("Accept", "application/json");

        var response = await client.GetStringAsync("https://icanhazdadjoke.com/");

        var result = JsonSerializer.Deserialize<Dictionary<string, object>>(response);

        return result["joke"].ToString();
    }
}

await Main();