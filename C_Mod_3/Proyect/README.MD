In terms of source control, you're "downstream" when you copy (clone, checkout, etc) from a repository. Information is flowed "downstream" to you.

When you make changes, you usually want to send them back "upstream" so they make it into that repository so that everyone pulling from the same source is working with all the same changes. This is mostly a social issue of how everyone can coordinate their work rather than a technical requirement of source control. You want to get your changes into the main project so you're not tracking divergent lines of development.
Setting the upstream for a fork you have created using the following command:

```git
git remote add upstream https://github.com/[git-username]/it-cert-automation-practice.git
```
If you want to clone the repository into another directory of your choice, you can do that by passing the name of the directory. This automatically creates a new directory with the specified name and initializes the repository inside it.

Syntax:
```
git clone [URL] directory_name
```