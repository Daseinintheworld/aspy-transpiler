import sys, io, contextlib, signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Execution timed out.")

def execute_safely(code: str, timeout=3):
    output = io.StringIO()
    sys_stdout = sys.stdout
    restricted_globals = {"__builtins__": {"print": print, "range": range, "input": input}}

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        with contextlib.redirect_stdout(output):
            exec(code, restricted_globals)
    except TimeoutException as e:
        return f"⏳ {e}"
    except Exception as e:
        return f"❌ Error: {e}"
    finally:
        signal.alarm(0)
        sys.stdout = sys_stdout

    return output.getvalue()
