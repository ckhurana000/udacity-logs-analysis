# Logging helper utility

# Reference prefixes
prefixes = ["Verbose", "Debug", "ExcessInfo", "MinimalInfo", "FatalWarn", "FatalError", "CriticalError",]

def print_log(prefix, log):
  print(prefix + " ", log)
