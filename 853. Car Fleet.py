class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        vehicles = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
        for mile, speed in vehicles:
            if not stack:
                stack.append((mile, speed))
                continue
            stack_mile, stack_speed = stack[-1]
            delta_speed = (speed - stack_speed)
            if delta_speed == 0:
                stack.append((mile, speed))
                continue
            time = (stack_mile - mile) / delta_speed
            if time < 0 or (time * stack_speed + stack_mile) > target:
                stack.append((mile, speed))

        return len(stack)
