
import click 
import just_count.square

@click.command()
@click.argument("x", type=int)

def main(x):
    print(f"The square of your number is {just_count.square.square(x)}")


if __name__ == "__main__":
    main()