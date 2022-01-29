GET-PACKAGE-VERSION-README()                      GET-PACKAGE-VERSION-README()



NAME
       get-package-version-readme -

DESCRIPTION
       Gets  the  readme  file  or descriptive text for a package version. For
       packages that do not contain a readme file, CodeArtifact extracts a de-
       scription from a metadata file. For example, from the <description> el-
       ement in the pom.xml file of a Maven package.

       The returned text might contain formatting. For example, it might  con-
       tain formatting for Markdown or reStructuredText.

       See also: AWS API Documentation

       See 'aws help' for descriptions of global parameters.

SYNOPSIS
            get-package-version-readme
          --domain <value>
          [--domain-owner <value>]
          --repository <value>
          --format <value>
          [--namespace <value>]
          --package <value>
          --package-version <value>
          [--cli-input-json | --cli-input-yaml]
          [--generate-cli-skeleton <value>]

OPTIONS
       --domain (string)
          The  name  of  the domain that contains the repository that contains
          the package version with the requested readme file.

       --domain-owner (string)
          The 12-digit account number of the AWS account that owns the domain.
          It does not include dashes or spaces.

       --repository (string)
          The  repository  that contains the package with the requested readme
          file.

       --format (string)
          A format that specifies the type of the package version with the re-
          quested readme file. The valid values are:

          o npm

          o pypi

          o maven

          Possible values:

          o npm

          o pypi

          o maven

          o nuget

       --namespace (string)
          The  namespace  of the package. The package component that specifies
          its namespace depends on its type. For example:

          o The namespace of a Maven package is its groupId .

          o The namespace of an npm package is its scope .

          o A Python package does not contain a  corresponding  component,  so
            Python packages do not have a namespace.

       --package (string)
          The  name  of the package version that contains the requested readme
          file.

       --package-version (string)
          A string that contains the package version (for example, 3.5.2 ).

       --cli-input-json | --cli-input-yaml (string) Reads arguments  from  the
       JSON  string  provided.  The JSON string follows the format provided by
       --generate-cli-skeleton. If other arguments are provided on the command
       line,  those  values  will override the JSON-provided values. It is not
       possible to pass arbitrary binary values using a JSON-provided value as
       the  string  will  be  taken literally. This may not be specified along
       with --cli-input-yaml.

       --generate-cli-skeleton (string) Prints a  JSON  skeleton  to  standard
       output without sending an API request. If provided with no value or the
       value input, prints a sample input JSON that can be used as an argument
       for --cli-input-json. Similarly, if provided yaml-input it will print a
       sample input YAML that can be used with --cli-input-yaml.  If  provided
       with  the  value  output, it validates the command inputs and returns a
       sample output JSON for that command.

       See 'aws help' for descriptions of global parameters.

EXAMPLES
       To get a package version's readme file

       The following get-package-version-readme example retrieves  the  readme
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

       For  more  information, see View package version readme file in the AWS
       CodeArtifact User Guide.

OUTPUT
       format -> (string)
          The format of the package with the requested readme file. Valid for-
          mat types are:

          o npm

          o pypi

          o maven

       namespace -> (string)
          The  namespace  of the package. The package component that specifies
          its namespace depends on its type. For example:

          o The namespace of a Maven package is its groupId .

          o The namespace of an npm package is its scope .

          o A Python package does not contain a  corresponding  component,  so
            Python packages do not have a namespace.

       package -> (string)
          The name of the package that contains the returned readme file.

       version -> (string)
          The version of the package with the requested readme file.

       versionRevision -> (string)
          The current revision associated with the package version.

       readme -> (string)
          The text of the returned readme file.



                                                  GET-PACKAGE-VERSION-README()
