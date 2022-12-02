Worklog
========
> Personal event logging for major and minor details

Worklog is a tool that accepts text input, organises it into a
dicionary organised by date and time. That's it.

Worklog was written to log simpler, invisible or lesser acknowledged
aspects of the workday. This means everything between "chat with Máire
about API onboarding workflow" to specific commands run in the process
of a multi-stage task.

The generated worklog was designed to be a way of working in parallel
and contributing to a [brag
document](https://jvns.ca/blog/brag-documents/). There's many aspects
of [glue work](https://noidea.dog/glue) that can be missed: they don't
end up on tickets and may be forgotten when it comes to writing
performance reviews or even just enumerating the ways in which you and
those you work with contributed to larger projects.

Worklog accepts input as a command line argument or via stdin. This
means worklog is a handy way to log the output of commands (when used
with the --tee argument so as to not silence output).

Operation
----------
Log an arbitrary message on the commandline:
```
$ worklog "Second pass at architecture review document diagrams"
Logged message at 20:26:15
```

Via stdin:
```
$ echo "Spun around in my chair a bunch" | worklog
Logged message at 20:26:39
```

Capture a command:
```
echo "lmao" | toilet | worklog
Logged message at 20:27:01
```

Worklog defaults to saving the log at ~/.worklog.yaml.

The log is stored as a simple dictionary of dictionaries keyed by date
and time respectively.

Configuration
-------------
[Faic](https://www.teanglann.ie/en/fgb/faic).

Author
----------
Hugh Nowlan <nosmo@nosmo.me>
