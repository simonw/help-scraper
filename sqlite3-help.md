# sqlite3 .help
```
.archive ...             Manage SQL archives
   Each command must have exactly one of the following options:
     -c, --create               Create a new archive
     -u, --update               Add or update files with changed mtime
     -i, --insert               Like -u but always add even if unchanged
     -t, --list                 List contents of archive
     -x, --extract              Extract files from archive
   Optional arguments:
     -v, --verbose              Print each filename as it is processed
     -f FILE, --file FILE       Use archive FILE (default is current db)
     -a FILE, --append FILE     Open FILE using the apndvfs VFS
     -C DIR, --directory DIR    Read/extract files from directory DIR
     -n, --dryrun               Show the SQL that would have occurred
   Examples:
     .ar -cf ARCHIVE foo bar  # Create ARCHIVE from files foo and bar
     .ar -tf ARCHIVE          # List members of ARCHIVE
     .ar -xvf ARCHIVE         # Verbosely extract files from ARCHIVE
   See also:
      http://sqlite.org/cli.html#sqlar_archive_support

.auth ON|OFF             Show authorizer callbacks

.backup ?DB? FILE        Backup DB (default "main") to FILE
       --append            Use the appendvfs
       --async             Write to FILE without journal and fsync()

.bail on|off             Stop after hitting an error.  Default OFF

.binary on|off           Turn binary output on or off.  Default OFF

.cd DIRECTORY            Change the working directory to DIRECTORY

.changes on|off          Show number of rows changed by SQL

.check GLOB              Fail if output since .testcase does not match

.clone NEWDB             Clone data into NEWDB from the existing database

.databases               List names and files of attached databases

.dbconfig ?op? ?val?     List or change sqlite3_db_config() options

.dbinfo ?DB?             Show status information about the database

.dump ?TABLE? ...        Render all database content as SQL
   Options:
     --preserve-rowids      Include ROWID values in the output
     --newlines             Allow unescaped newline characters in output
   TABLE is a LIKE pattern for the tables to dump

.echo on|off             Turn command echo on or off

.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
   Other Modes:
      trigger               Like "full" but also show trigger bytecode

.excel                   Display the output of next command in spreadsheet

.exit ?CODE?             Exit this program with return-code CODE

.expert                  EXPERIMENTAL. Suggest indexes for queries

.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto

.filectrl CMD ...        Run various sqlite3_file_control() operations
                           Run ".filectrl" with no arguments for details

.fullschema ?--indent?   Show schema and the content of sqlite_stat tables

.headers on|off          Turn display of headers on or off

.help ?-all? ?PATTERN?   Show help text for PATTERN

.import FILE TABLE       Import data from FILE into TABLE

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

.mode MODE ?TABLE?       Set output mode
   MODE is one of:
     ascii    Columns/rows delimited by 0x1F and 0x1E
     csv      Comma-separated values
     column   Left-aligned columns.  (See .width)
     html     HTML <table> code
     insert   SQL insert statements for TABLE
     line     One value per line
     list     Values delimited by "|"
     quote    Escape answers as for SQL
     tabs     Tab-separated values
     tcl      TCL list elements

.nullvalue STRING        Use STRING in place of NULL values

.once (-e|-x|FILE)       Output for the next SQL command only to FILE
     If FILE begins with '|' then open as a pipe
     Other options:
       -e    Invoke system text editor
       -x    Open in a spreadsheet

.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
     Options:
        --append        Use appendvfs to append database to the end of FILE
        --deserialize   Load into memory useing sqlite3_deserialize()
        --hexdb         Load the output of "dbtotxt" as an in-memory db
        --maxsize N     Maximum size for --hexdb or --deserialized database
        --new           Initialize FILE to an empty database
        --nofollow      Do not follow symbolic links
        --readonly      Open FILE readonly
        --zip           FILE is a ZIP archive

.output ?FILE?           Send output to FILE or stdout if FILE is omitted
     If FILE begins with '|' then open it as a pipe.

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

.read FILE               Read input from FILE

.recover                 Recover as much data as possible from corrupt db.
   --freelist-corrupt       Assume the freelist is corrupt
   --recovery-db NAME       Store recovery metadata in database file NAME
   --lost-and-found TABLE   Alternative name for the lost-and-found table
   --no-rowids              Do not attempt to recover rowid values
                            that are not also INTEGER PRIMARY KEYs

.restore ?DB? FILE       Restore content of DB (default "main") from FILE

.save FILE               Write in-memory database into FILE

.scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off

.schema ?PATTERN?        Show the CREATE statements matching PATTERN
     Options:
         --indent            Try to pretty-print the schema

.selftest ?OPTIONS?      Run tests defined in the SELFTEST table
    Options:
       --init               Create a new SELFTEST table
       -v                   Verbose output

.separator COL ?ROW?     Change the column and row separators

.session ?NAME? CMD ...  Create or control sessions
   Subcommands:
     attach TABLE             Attach TABLE
     changeset FILE           Write a changeset into FILE
     close                    Close one session
     enable ?BOOLEAN?         Set or query the enable bit
     filter GLOB...           Reject tables matching GLOBs
     indirect ?BOOLEAN?       Mark or query the indirect status
     isempty                  Query whether the session is empty
     list                     List currently open session names
     open DB NAME             Open a new session on DB
     patchset FILE            Write a patchset into FILE
   If ?NAME? is omitted, the first defined session is used.

.sha3sum ...             Compute a SHA3 hash of database content
    Options:
      --schema              Also hash the sqlite_master table
      --sha3-224            Use the sha3-224 algorithm
      --sha3-256            Use the sha3-256 algorithm (default)
      --sha3-384            Use the sha3-384 algorithm
      --sha3-512            Use the sha3-512 algorithm
    Any other argument is a LIKE pattern for tables to hash

.shell CMD ARGS...       Run CMD ARGS... in a system shell

.show                    Show the current values for various settings

.stats ?on|off?          Show stats or turn stats on or off

.system CMD ARGS...      Run CMD ARGS... in a system shell

.tables ?TABLE?          List names of tables matching LIKE pattern TABLE

.check GLOB              Fail if output since .testcase does not match
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

.mode MODE ?TABLE?       Set output mode
   MODE is one of:
     ascii    Columns/rows delimited by 0x1F and 0x1E
     csv      Comma-separated values
     column   Left-aligned columns.  (See .width)
     html     HTML <table> code
     insert   SQL insert statements for TABLE
     line     One value per line
     list     Values delimited by "|"
     quote    Escape answers as for SQL
     tabs     Tab-separated values
     tcl      TCL list elements
.width NUM1 NUM2 ...     Set column widths for "column" mode
     Negative values right-justify
```
