"use client";

import { useRouter } from "next/navigation";
import { useAuth } from "@clerk/nextjs";
import { useUser } from '@clerk/nextjs'

export default function HomePage() {
  const router = useRouter();

  const { isLoaded, isSignedIn } = useAuth();
  const { user } = useUser();

  console.log(user?.fullName);

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white dark:from-gray-900 dark:to-gray-800 px-4 py-16">
      <div className="max-w-4xl mx-auto">
        {user?.fullName ? (
          <h1 className="text-5xl md:text-6xl font-bold mb-8 text-center bg-gradient-to-r from-blue-600 to-purple-600 text-transparent bg-clip-text">
            Welcome, {user?.fullName}
          </h1>
        ) : (
          <h1 className="text-5xl md:text-6xl font-bold mb-8 text-center bg-gradient-to-r from-blue-600 to-purple-600 text-transparent bg-clip-text">
            Welcome to BrightMind
          </h1>
        )}

        <div className="space-y-8">
          <section className="bg-white/80 dark:bg-gray-800/90 rounded-xl p-8 shadow-lg backdrop-blur-sm border border-gray-100 dark:border-gray-700">
            <h2 className="text-3xl font-semibold mb-6 text-blue-600 dark:text-blue-400">
              Your Journey to Mental Wellness
            </h2>
            <p className="text-gray-700 dark:text-gray-300 mb-6 text-lg leading-relaxed">
              BrightMind provides a safe, supportive space for your mental
              health journey. Discover tools, resources, and guidance to enhance
              your emotional well-being.
            </p>
            <div className="flex gap-4 flex-wrap">
              <button
                className="flex-1 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white px-8 py-3 rounded-lg text-lg font-medium transition-all duration-300 transform hover:scale-105 shadow-md"
                onClick={() => router.push("/mood-check")}
              >
                How are you feeling today?
              </button>
              {isSignedIn && (
                <button
                  className="flex-1 bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white px-8 py-3 rounded-lg text-lg font-medium transition-all duration-300 transform hover:scale-105 shadow-md"
                  onClick={() => router.push("/talk")}
                >
                  Want to talk? Chat with us.
                </button>
              )}
            </div>
          </section>

          <section className="grid md:grid-cols-2 gap-8">
            <div
              className="bg-white/80 dark:bg-gray-800/90 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 backdrop-blur-sm border border-gray-100 dark:border-gray-700 cursor-pointer"
              onClick={() => router.push("/wellness-resource")}
            >
              <h3 className="text-2xl font-semibold mb-4 text-blue-600 dark:text-blue-400 cursor-pointer">
                Wellness Resources
              </h3>
              <p className="text-gray-700 dark:text-gray-300 text-lg leading-relaxed">
                Access expert-curated content on mindfulness, stress management,
                and emotional resilience.
              </p>
            </div>

            <div className="bg-white/80 dark:bg-gray-800/90 rounded-xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 backdrop-blur-sm border border-gray-100 dark:border-gray-700 cursor-pointer"
              onClick={() => router.push("/support-pathway")}
            >
              <h3 className="text-2xl font-semibold mb-4 text-blue-600 dark:text-blue-400">
                Support Pathways
              </h3>
              <p className="text-gray-700 dark:text-gray-300 text-lg leading-relaxed">
                Discover personalized mental health support options and guided
                self-help programs.
              </p>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}
