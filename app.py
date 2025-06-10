import click

@click.command()
@click.argument('logfile', type=click.Path(exists=True))

# Summarize log file by extracting key events
def summarize(logfile):
    try: 
        with open(logfile, "r") as f:
            content = f.readlines()

        infos = [line for line in content if "INFO" in line]
        warnings = [line for line in content if "WARN" in line or "WARNING" in line]
        errors = [line for line in content if "ERROR" in line]

        print(f"\nSummary of {logfile}:\n")
        print(f"Total lines: {len(content)}")
        print(f"Info messages: {len(infos)}")
        print(f"Warnings: {len(warnings)}")
        print(f"Errors: {len(errors)}\n")

        if infos:
            print("Sample Info:")
            print(infos[0])

        if warnings:
            print("Sample Warning:")
            print(warnings[0])

        if errors:
            print("Sample Error:")
            print(errors[0])
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    summarize()