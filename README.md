# help-scraper

Record a history of `--help` for various commands

See [Help scraping: track changes to CLI tools by recording their --help using Git](https://simonwillison.net/2022/Feb/2/help-scraping/) for the background of this project.

This repository installs tools and records the output of their `--help` commands, to track changes made to them over time.

- [flyctl/](flyctl/) - the [flyctl](https://github.com/superfly/flyctl/) management tool by [Fly.io](https://fly.io/)
- [aws/](aws/) - the Amazon Web Services [CLI interface](https://aws.amazon.com/cli/)
- [vercel/](vercel/) - the `vercel` management tool by [Vercel](https://vercel.com/)

The repo also tracks changes made to some GraphQL schemas:

- [flyctl/fly.graphql](flyctl/fly.graphql) for `https://api.fly.io/graphql`
- [github/github.graphql](github/github.graphql) for `https://api.github.com/graphql`
