# sqlite3 .help

Version: `3.39.0 2022-04-13 12:34:54 fa9d206f904280e3eafc6f4ba6c0c7325948364c62eeeb9f0fdc5825d622ec35`

```
.auth ON|OFF             Show authorizer callbacks

.backup ?DB? FILE        Backup DB (default "main") to FILE
   Options:
       --append            Use the appendvfs
       --async             Write to FILE without journal and fsync()

.bail on|off             Stop after hitting an error.  Default OFF

.binary on|off           Turn binary output on or off.  Default OFF

.cd DIRECTORY            Change the working directory to DIRECTORY

.changes on|off          Show number of rows changed by SQL

.check GLOB              Fail if output since .testcase does not match

.clone NEWDB             Clone data into NEWDB from the existing database

.connection [close] [#]  Open or close an auxiliary database connection

.databases               List names and files of attached databases

.dbconfig ?op? ?val?     List or change sqlite3_db_config() options

.dbinfo ?DB?             Show status information about the database

.dump ?OBJECTS?          Render database content as SQL
   Options:
     --data-only            Output only INSERT statements
     --newlines             Allow unescaped newline characters in output
     --nosys                Omit system tables (ex: "sqlite_stat1")
     --preserve-rowids      Include ROWID values in the output
   OBJECTS is a LIKE pattern for tables, indexes, triggers or views to dump
   Additional LIKE patterns can be given in subsequent arguments

.echo on|off             Turn command echo on or off

.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
   Other Modes:
      trigger               Like "full" but also show trigger bytecode

.excel                   Display the output of next command in spreadsheet
   --bom                   Put a UTF8 byte-order mark on intermediate file

.exit ?CODE?             Exit this program with return-code CODE

.expert                  EXPERIMENTAL. Suggest indexes for queries

.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto

.filectrl CMD ...        Run various sqlite3_file_control() operations
   --schema SCHEMA         Use SCHEMA instead of "main"
   --help                  Show CMD details

.fullschema ?--indent?   Show schema and the content of sqlite_stat tables

.headers on|off          Turn display of headers on or off

.help ?-all? ?PATTERN?   Show help text for PATTERN

.import FILE TABLE       Import data from FILE into TABLE
   Options:
     --ascii               Use \037 and \036 as column and row separators
     --csv                 Use , and \n as column and row separators
     --skip N              Skip the first N rows of input
     --schema S            Target table to be S.TABLE
     -v                    "Verbose" - increase auxiliary output
   Notes:
     *  If TABLE does not exist, it is created.  The first row of input
        determines the column names.
     *  If neither --csv or --ascii are used, the input mode is derived
        from the ".mode" output mode
     *  If FILE begins with "|" then it is a command that generates the
        input text.

.imposter INDEX TABLE    Create imposter table TABLE on index INDEX

.indexes ?TABLE?         Show names of indexes
                           If TABLE is specified, only show indexes for
                           tables matching TABLE using the LIKE operator.

.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT

.lint OPTIONS            Report potential schema issues.
     Options:
        fkey-indexes     Find missing foreign key indexes

.load FILE ?ENTRY?       Load an extension library

.log FILE|off            Turn logging on or off.  FILE can be stderr/stdout

.mode MODE ?OPTIONS?     Set output mode
   MODE is one of:
     ascii       Columns/rows delimited by 0x1F and 0x1E
     box         Tables using unicode box-drawing characters
     csv         Comma-separated values
     column      Output in columns.  (See .width)
     html        HTML <table> code
     insert      SQL insert statements for TABLE
     json        Results in a JSON array
     line        One value per line
     list        Values delimited by "|"
     markdown    Markdown table format
     qbox        Shorthand for "box --width 60 --quote"
     quote       Escape answers as for SQL
     table       ASCII-art table
     tabs        Tab-separated values
     tcl         TCL list elements
   OPTIONS: (for columnar modes or insert mode):
     --wrap N       Wrap output lines to no longer than N characters
     --wordwrap B   Wrap or not at word boundaries per B (on/off)
     --ww           Shorthand for "--wordwrap 1"
     --quote        Quote output text as SQL literals
     --noquote      Do not quote output text
     TABLE          The name of SQL table used for "insert" mode

.nonce STRING            Suspend safe mode for one command if nonce matches

.nullvalue STRING        Use STRING in place of NULL values

.once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
     If FILE begins with '|' then open as a pipe
       --bom  Put a UTF8 byte-order mark at the beginning
       -e     Send output to the system text editor
       -x     Send output as CSV to a spreadsheet (same as ".excel")

.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
     Options:
        --append        Use appendvfs to append database to the end of FILE
        --deserialize   Load into memory using sqlite3_deserialize()
        --hexdb         Load the output of "dbtotxt" as an in-memory db
        --maxsize N     Maximum size for --hexdb or --deserialized database
        --new           Initialize FILE to an empty database
        --nofollow      Do not follow symbolic links
        --readonly      Open FILE readonly
        --zip           FILE is a ZIP archive

.output ?FILE?           Send output to FILE or stdout if FILE is omitted
   If FILE begins with '|' then open it as a pipe.
   Options:
     --bom                 Prefix output with a UTF8 byte-order mark
     -e                    Send output to the system text editor
     -x                    Send output as CSV to a spreadsheet

.parameter CMD ...       Manage SQL parameter bindings
   clear                   Erase all bindings
   init                    Initialize the TEMP table that holds bindings
   list                    List the current parameter bindings
   set PARAMETER VALUE     Given SQL parameter PARAMETER a value of VALUE
                           PARAMETER should start with one of: $ : @ ?
   unset PARAMETER         Remove PARAMETER from the binding table

.print STRING...         Print literal STRING

.progress N              Invoke progress handler after every N opcodes
   --limit N                 Interrupt after N progress callbacks
   --once                    Do no more than one progress interrupt
   --quiet|-q                No output except at interrupts
   --reset                   Reset the count for each input and interrupt

.prompt MAIN CONTINUE    Replace the standard prompts

.quit                    Exit this program

.read FILE               Read input from FILE or command output
    If FILE begins with "|", it is a command that generates the input.

.restore ?DB? FILE       Restore content of DB (default "main") from FILE

.save ?OPTIONS? FILE     Write database to FILE (an alias for .backup ...)

.scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off

.schema ?PATTERN?        Show the CREATE statements matching PATTERN
   Options:
      --indent             Try to pretty-print the schema
      --nosys              Omit objects whose names start with "sqlite_"

.selftest ?OPTIONS?      Run tests defined in the SELFTEST table
    Options:
       --init               Create a new SELFTEST table
       -v                   Verbose output

.separator COL ?ROW?     Change the column and row separators

.sha3sum ...             Compute a SHA3 hash of database content
    Options:
      --schema              Also hash the sqlite_schema table
      --sha3-224            Use the sha3-224 algorithm
      --sha3-256            Use the sha3-256 algorithm (default)
      --sha3-384            Use the sha3-384 algorithm
      --sha3-512            Use the sha3-512 algorithm
    Any other argument is a LIKE pattern for tables to hash

.shell CMD ARGS...       Run CMD ARGS... in a system shell

.show                    Show the current values for various settings

.stats ?ARG?             Show stats or turn stats on or off
   off                      Turn off automatic stat display
   on                       Turn on automatic stat display
   stmt                     Show statement stats
   vmstep                   Show the virtual machine step count only

.system CMD ARGS...      Run CMD ARGS... in a system shell

.tables ?TABLE?          List names of tables matching LIKE pattern TABLE

.testcase NAME           Begin redirecting output to 'testcase-out.txt'

.testctrl CMD ...        Run various sqlite3_test_control() operations
                           Run ".testctrl" with no arguments for details

.timeout MS              Try opening locked tables for MS milliseconds

.timer on|off            Turn SQL timer on or off

.trace ?OPTIONS?         Output each SQL statement as it is run
    FILE                    Send output to FILE
    stdout                  Send output to stdout
    stderr                  Send output to stderr
    off                     Disable tracing
    --expanded              Expand query parameters
    --plain                 Show SQL as it is input
    --stmt                  Trace statement execution (SQLITE_TRACE_STMT)
    --profile               Profile statements (SQLITE_TRACE_PROFILE)
    --row                   Trace each row (SQLITE_TRACE_ROW)
    --close                 Trace connection close (SQLITE_TRACE_CLOSE)

.vfsinfo ?AUX?           Information about the top-level VFS

.vfslist                 List all available VFSes

.vfsname ?AUX?           Print the name of the VFS stack

.width NUM1 NUM2 ...     Set minimum column widths for columnar output
```
