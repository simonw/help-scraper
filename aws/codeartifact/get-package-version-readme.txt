GET-PACKAGE-VERSION-README()                      GET-PACKAGE-VERSION-README()



NAME
       get-package-version-readme -

DESCRIPTION
       Gets the readme file or descriptive text for a package version.

       The  returned text might contain formatting. For example, it might con-
       tain formatting for Markdown or reStructuredText.

       See also: AWS API Documentation

SYNOPSIS
            get-package-version-readme
          --domain <value>
          [--domain-owner <value>]
          --repository <value>
          --format <value>
          [--namespace <value>]
          --package <value>
          --package-version <value>
          [--cli-input-json <value>]
          [--generate-cli-skeleton <value>]
          [--debug]
          [--endpoint-url <value>]
          [--no-verify-ssl]
          [--no-paginate]
          [--output <value>]
          [--query <value>]
          [--profile <value>]
          [--region <value>]
          [--version <value>]
          [--color <value>]
          [--no-sign-request]
          [--ca-bundle <value>]
          [--cli-read-timeout <value>]
          [--cli-connect-timeout <value>]

OPTIONS
       --domain (string)
          The name of the domain that contains the  repository  that  contains
          the package version with the requested readme file.

       --domain-owner (string)
          The  12-digit account number of the Amazon Web Services account that
          owns the domain. It does not include dashes or spaces.

       --repository (string)
          The repository that contains the package with the  requested  readme
          file.

       --format (string)
          A format that specifies the type of the package version with the re-
          quested readme file.

          Possible values:

          o npm

          o pypi

          o maven

          o nuget

          o generic

       --namespace (string)
          The namespace of the package version with the requested readme file.
          The  package  version component that specifies its namespace depends
          on its type. For example:

          o The namespace of an npm package version is its scope .

          o Python and NuGet package versions do not contain  a  corresponding
            component,  package  versions of those formats do not have a name-
            space.

       --package (string)
          The name of the package version that contains the  requested  readme
          file.

       --package-version (string)
          A string that contains the package version (for example, 3.5.2 ).

       --cli-input-json  (string) Performs service operation based on the JSON
       string provided. The JSON string follows the format provided by  --gen-
       erate-cli-skeleton.  If  other  arguments  are  provided on the command
       line, the CLI values will override the JSON-provided values. It is  not
       possible to pass arbitrary binary values using a JSON-provided value as
       the string will be taken literally.

       --generate-cli-skeleton (string) Prints a  JSON  skeleton  to  standard
       output without sending an API request. If provided with no value or the
       value input, prints a sample input JSON that can be used as an argument
       for  --cli-input-json.  If provided with the value output, it validates
       the command inputs and returns a sample output JSON for that command.

GLOBAL OPTIONS
       --debug (boolean)

       Turn on debug logging.

       --endpoint-url (string)

       Override command's default URL with the given URL.

       --no-verify-ssl (boolean)

       By default, the AWS CLI uses SSL when communicating with AWS  services.
       For each SSL connection, the AWS CLI will verify SSL certificates. This
       option overrides the default behavior of verifying SSL certificates.

       --no-paginate (boolean)

       Disable automatic pagination.

       --output (string)

       The formatting style for command output.

       o json

       o text

       o table

       --query (string)

       A JMESPath query to use in filtering the response data.

       --profile (string)

       Use a specific profile from your credential file.

       --region (string)

       The region to use. Overrides config/env settings.

       --version (string)

       Display the version of this tool.

       --color (string)

       Turn on/off color output.

       o on

       o off

       o auto

       --no-sign-request (boolean)

       Do not sign requests. Credentials will not be loaded if  this  argument
       is provided.

       --ca-bundle (string)

       The CA certificate bundle to use when verifying SSL certificates. Over-
       rides config/env settings.

       --cli-read-timeout (int)

       The maximum socket read time in seconds. If the value is set to 0,  the
       socket  read  will be blocking and not timeout. The default value is 60
       seconds.

       --cli-connect-timeout (int)

       The maximum socket connect time in seconds. If the value is set  to  0,
       the  socket connect will be blocking and not timeout. The default value
       is 60 seconds.

EXAMPLES
       NOTE:
          To use the following examples, you must have the AWS  CLI  installed
          and  configured.  See  the Getting started guide in the AWS CLI User
          Guide for more information.

          Unless otherwise  stated,  all  examples  have  unix-like  quotation
          rules.  These  examples  will  need to be adapted to your terminal's
          quoting rules. See Using quotation marks with strings in the AWS CLI
          User Guide .

       To get a package version's readme file

       The  following  get-package-version-readme example retrieves the readme
       file for version 4.0.0 of an npm package named test-package.

          aws codeartifact get-package-version-readme \
              --domain test-domain \
              --repo test-repo \
              --format npm \
              --package test-package \
              --package-version 4.0.0

       Output:

          {
              "format": "npm",
              "package": "test-package",
              "version": "4.0.0",
              "readme": "<div align=\"center\">\n   <a href=\https://github.com/test-package/testpack\"> ... more content ... \n",
              "versionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs="
          }

       For more information, see View package version readme file in  the  AWS
       CodeArtifact User Guide.

OUTPUT
       format -> (string)
          The format of the package with the requested readme file.

       namespace -> (string)
          The namespace of the package version with the requested readme file.
          The package version component that specifies its  namespace  depends
          on its type. For example:

          o The namespace of a Maven package version is its groupId .

          o The namespace of an npm package version is its scope .

          o Python  and  NuGet package versions do not contain a corresponding
            component, package versions of those formats do not have  a  name-
            space.

       package -> (string)
          The name of the package that contains the returned readme file.

       version -> (string)
          The version of the package with the requested readme file.

       versionRevision -> (string)
          The current revision associated with the package version.

       readme -> (string)
          The text of the returned readme file.



                                                  GET-PACKAGE-VERSION-README()
