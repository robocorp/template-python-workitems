# Python based template for producer-consumer model robots using work items

This template leverages the new python open-source structure [robo](https://github.com/robocorp/robo), the [libraries](https://github.com/robocorp/robo#libraries) from to same project as well.

The template provides you with the basic structure of a Python project: logging out of the box and controlling your tasks without fiddling with the base Python stuff. The environment contains the most used libraries, so you do not have to start thinking about those right away. 
With `robocorp-workitems`, you can just start creating and consuming workitems for your process steps.

👉 After running the bot, check out the `log.html` under the `output` -folder.

This template contains a working robot implementation that has the basic structure where one part produces work items from input and another part that consumes those work items. 

> The [producer-consumer](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem) model is not limited to two steps, it can continue so that the consumer generates further work items for the next step and so on.

The template tries to keep the amount of functional code at a minimum so you have less to clear out and replace with your own implementation, but some functional logic is needed to have the template working and guiding the key parts.

> We recommended checking out the article "[Using work items](https://robocorp.com/docs/development-guide/control-room/work-items)" before diving in.


## Tasks

The robot is split into two tasks, meant to run as separate steps in Control Room. The first task generates (produces) data, and the second one reads (consumes) and processes that data.

### The first task (the producer)

- Load the example Excel file from work item
- Splits the Excel file into work items for the consumer

### The second task (the consumer)

> We recommended checking out the article "[Work item exception handling](https://robocorp.com/docs/development-guide/control-room/work-items#work-item-exception-handling)" before diving in.

- A simulated "Login" step.
  - This simulates random failures to highlight the use of `APPLICATION` -exception type.
- Loop that handles the work items and just creates a logs row for each
  - This simulates random failures to highlight the use of `BUSINESS` -exception type.

### Local testing

For best experience to test the work items in this example we recommend using [our VS Code extensions](https://robocorp.com/docs/developer-tools/visual-studio-code). With the Robocorp Code extension you can simply run and [select the input work items](https://robocorp.com/docs/developer-tools/visual-studio-code/extension-features#using-work-items) to use, create inputs to simulate error cases and so on.



🚀 Now, you can just get to writing.

For more information, do not forget to checkout the following:
* [Robocorp Documentation -site](https://robocorp.com/docs)
* [Portal for more examples](https://robocorp.com/portal)
* [robo repo](https://github.com/robocorp/robo) as this will developed a lot...