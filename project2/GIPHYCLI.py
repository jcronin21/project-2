import click
import os
import requests

API_KEY = os.environ.get("GIPHY_API_KEY") 

@click.group()
def gif():
    pass

@gif.command()
@click.option("--count", default=3, help="this is going to show 3 results")
@click.option("--lucky", is_flag=True, help="im feelin lucky")

def trending(count,lucky):
    url = f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit={count}&rating=g"
    response = requests.get(url)
    data = response.json()["data"]
    if lucky:
        gif = data[0] 
        click.echo(f"![{gif['title']}]({gif['url']})")
    else:
         counter = 1
    for gif in data[:count]: 
        #counter += counter +1
        click.echo("{}{}) {} ({}) ".format(counter,')', gif['title'], gif['url']))
        counter += 1

   
@gif.command()
@click.option("--count", default=3, help="showing 3 results")
@click.option("--markdown", is_flag=True, help="markdown content")
@click.option("--lucky", is_flag=True, help="im feelin lucky")
@click.argument("query")

def search(count, query,markdown,lucky):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={query}&limit={count}&rating=g"
    response = requests.get(url)
    data = response.json()["data"]
    if count:
        # counter = counter+1
        counter = 1
        for gif in data:
            click.echo(f"{counter}) {gif['title']} ({gif['url']})")
            counter += 1
            if markdown:
                click.echo(f"![{gif['title']}]({gif['url']})")
            if lucky:
                click.echo(f"![{gif['title']}]({gif['url']})")
                break
    else:
        click.echo("somethings not right")


   




if __name__ == "__main__":
    gif()


#chat gpt helped me format