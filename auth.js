import { auth } from "@/auth";
import NextAuth from "next-auth"

jest.mock("@/auth", () => ({
  auth: jest.fn(),
}));

describe("Protected Component or Page", () => {
  it("returns session data when authenticated", async () => {
    // Stub a fake logged-in user session
    auth.mockResolvedValue({
      user: { name: "Test User", email: "test@example.com" },
    });

    const session = await auth();
    expect(session.user.name).toBe("Test User");
  });

  it("returns null when not authenticated", async () => {
    // Stub an unauthenticated state
    auth.mockResolvedValue(null);

    const session = await auth();
    expect(session).toBeNull();
  });
});
